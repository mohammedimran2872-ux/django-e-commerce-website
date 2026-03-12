from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# register=User.objects.all()
# for i in register:
#     print(i.email)

def main(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user.username
        print(f"uswer is logged and v=nav name is {user}")
        try:
            customer = User_Login.objects.get(name = user)
            nav_coin = customer.coins
            print(f"customer name os {customer}")
            print(f'customer coins {nav_coin}')
            context = {'customer':customer, "coins" : nav_coin}
        except:
            print("customer nit fount")
    return render (request, 'main.html', context)

def nav(request):
    if request.user.is_authenticated:
        user = request.user.username
        print(f"uswer is logged and v=nav name is {user}")
        try:
            customer = User_Login.objects.get(name = user)
            nav_coin = customer.coins
            print(f"customer name os {customer}")
            print(f'customer coins {nav_coin}')
            context = {'customer':customer, "coins" : nav_coin}
        except:
            print("customer nit fount")
    return render (request, 'nav.html', context)


def win (request):
    return render (request, 'won.html')
# ------------------REGISTER FORM------------------>
def register(request):
    context = {}
    if request.method == 'POST':
        print("5555555555555555555555555")
        uname=request.POST.get('username')
        lname=request.POST.get('lastname')
        fname=request.POST.get('firstname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if User.objects.filter(username=uname).exists():
            # ❌ User already exists — send error message back
            messages =  'Username already exists! Please choose another.'
            print(messages)
            context = {"messages":messages}
            return render(request, 'register.html', context)
        a =User.objects.create_user(
            username=uname,
            last_name=lname,
            first_name=fname,
            email=email,
            password=password
        )

        a=User_Login(name=uname)
        a.save()
        return redirect ('/signin')
    return render (request, 'register.html')
users = User.objects.all()
pas = "developer"
for i in users:
    if i.username == "rasik" :
        print("user already exists")
        break
else:
    print("user does not exists")
    print("username alrady exists please enter another name")

# --------------------------LOGIN FORM ---------------------------->

def signin(request):
    
 
    if request.method == 'POST':
        
        login_username = request.POST.get('username')
        password = request.POST.get('password')

        print("hrereeeeeeeeeeeeeeeeeee")
        global user_verify      
        # authenticate the user login page------>  
        user_verify = authenticate(request, username=login_username, password=password)
        
        print(f"login user name{user_verify}---------------->")
        
        if user_verify is not None:
            print("the if conditional so very rude")
            login(request, user_verify) 
            return redirect('/main')   
        else:
            print("wwwwwwwwwwwwwwwwwwwwwwwwwww")
            return render(request, 'signin.html', {"error": "Invalid credentials"})

    return render(request, 'signin.html')



import random
num=random.randint(1000,9999)  
num=str(num)   

# ------------------------------GAME LOGICS------------------->

def game_page(request):
    
    user = request.user.username
    print(f"uswer is logged and v=nav name is {user}")
        
    customer = User_Login.objects.get(name = user)
    nav_coin = customer.coins
    
    print(f"customer name os {customer}")
    print(f'customer coins {nav_coin}')
    context = {'customer':customer, "coins" : nav_coin }
        
    latest_login = User_Login.objects.latest('id')
    # ---COINS----------->
   


    if request.method == 'POST' :
        attempt=0
        # current rows find-----
        print("excel of this perfrorm to the>>>>>>>>>>>")
        print(customer) 
        print("excel of this------------------- perfrorm to the  >>>>>>>>>")


        print(num)
           
        status="try again buddy"
        gscore=10
        hint=""
        
        user=request.POST.get('code')
        
        print(user)
        length=len(user)
        print(length)
       
        print(len(num))
        if (user != "" or length == 4):
                                                          
            attempt+=1
            # WIN RESULT-------------------->
            if user == num:
                gscore+=10
                hint="****"
                # print(hint)
                # add_coins=User_Login.coins+=150
                # print(add_coins)


                added=User_Login.objects.filter(name=customer).first()
                added.coins+=3000
                added.save()
                print(added)
                
                # coins_value = User_Login.objects.filter(name='ezhil').values_list('coins', flat=True).first()
                # print(coins_value)
                status="you win buddy"
                record={"attempt" : attempt, "hint": hint,"guess" : user, "status": status, "score":gscore, "coins": nav_coin} 
                print(record)

                gamere=GameRecord(name=customer, guess=user, attempt=attempt,
                                  status=status, score=gscore,)
                gamere.save()

                gamehis=GameHistory(name=latest_login, input=user, key=hint, 
                                 attempt=attempt, status=status)
                gamehis.save()
                # return  render (request, 'game.html', {"table" : record, "coins": coins_value,"shows": show_data} )
                return redirect('/win')
            else:
                
                for i in range(0, len(num)):
                    print(i)
                    if user[i] == num[i]:     
                        hint+="*"              
                    elif user[i] in num:
                        hint+="#"
                    else:
                        hint+="_"
     
            print("page double--------->")
            print(hint)
            gscore+=10
            

            record={"attempt" : attempt, "hint": hint, "status": status, "guess" : user}
            print(record)
            gamehis=GameHistory(name=latest_login, input=user, key=hint,
                                 attempt=attempt, status=status)
            gamehis.save()
            context = {'customer':customer, "coins" : nav_coin,"table" : record }
            return  render (request, 'game.html', context )

        else:
            return render(request, 'game.html', context)
        
    
    return render(request, 'game.html', context) 

        
def gamehistory(request):
    if request.user.is_authenticated:
        user = request.user.username
        if GameHistory.objects.filter(name=user).exists():
        
            game_history = GameHistory.objects.filter(name=user)
            print(game_history)
            messages = ""
            return render (request, 'gamehistory.html', {"gamehistory" : game_history, "username" : user, "messages":messages})

        else:
            messages = "history dosn't exists"

        return render (request, 'gamehistory.html', { "username" : user, "messages":messages})



# TOURNAMENT LIST------------------>
def tournament_list(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user.username

        print(f"uswer is logged and v=nav name is {user}")
        try:
            customer = User_Login.objects.get(name = user)
            customer.coins -=200
            customer.save()
            nav_coin = customer.coins
            

            print(f"customer name os {customer}")
            print(f'customer coins {nav_coin}')
            context = {'customer':customer, "coins" : nav_coin}
        except:
            print("customer nit fount")
    
    tournaments=Tournament.objects.all()
    context["tourlist"] = tournaments 

    return render (request, 'tournament_list.html', context)

# TOURNAMENT HISTORY-------------------------->
def tournament_history(request):


    return(request, 'tourlist_history.html')

