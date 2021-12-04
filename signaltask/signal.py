from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import (pre_init,pre_save,pre_delete,
                    post_init,post_save,post_delete)
from django.core.signals import request_started,request_finished,got_request_exception

# Oneway method 1
# def user_login(sender,request,user,**kwargs):
#     print("Sender" , sender)
#     print("request",request)
#     print("user",user)
#     print("kwargs",kwargs)

# user_logged_in.connect(user_login,sender=User)


@receiver(user_logged_in, sender=User)
def user_login(sender,request,user,**kwargs):
    print("Sender" , sender)
    print("request",request)
    print("user",user)
    print("kwargs",kwargs)

# user_logged_in.connect(user_login,sender=User)


@receiver(user_logged_out, sender=User)
def user_logout(sender,request,user,**kwargs):
    print("Log out")
    print("Sender" , sender)
    print("request",request)
    print("user",user)
    print("kwargs",kwargs)
# user_logged_out.connect(user_logout,sender=User)


@receiver(user_login_failed)
def user_logout_failed(sender,credentials,request,**kwargs):
    print("Login failed")
    print("Sender" , sender)
    print("request",request)
    print("credential",credentials)
    print("kwargs",kwargs)

#user_login_failed.connect()

@receiver(pre_save,sender=User)
def at_begining_save(sender,instance,**kwargs):
    print("------------------")
    print("PreSave -----------")
    print("sender" , sender)
    print("instace" , instance)
    print("kwargs" , kwargs)

# pre_save.connect(at_begining_save , sender=User)


@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("------------------")
        print("post_save -----------")
        print("New Record")
        print("sender" , sender)
        print("instace" , instance)
        print("created" , created)
        print("kwargs" , kwargs)
    else:
        print("----------")
        print("Update Record")

# post_save.connect(at_ending_save , sender=User)

@receiver(pre_delete, sender=User)
def at_begining_delete(sender,instance,**kwargs):
    print("-----------------")
    print("pre delete")
    print("sender",sender)
    print("Instance" ,instance)
    print("Kwargs" , kwargs)

# pre_delete.connect(at_begining_delete , sender=User)



@receiver(post_delete, sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("-----------------")
    print("pre delete")
    print("sender",sender)
    print("Instance" ,instance)
    print("Kwargs" , kwargs)

# post_delete.connect(at_ending_delete , sender=User)

@receiver(pre_init, sender=User)
def at_begining_init(sender,*args,**kwargs):
    print("-----------------")
    print("pre init")
    print("sender",sender)
    print("Instance" ,*args)
    print("Kwargs" , kwargs)

# pre_init.connect(at_begining_init , sender=User)


@receiver(post_init, sender=User)
def at_ending_init(sender,*args,**kwargs):
    print("-----------------")
    print("pre init")
    print("sender",sender)
    print("Instance" ,args)
    print("Kwargs" , kwargs)

# pre_init.connect(at_ending_init , sender=User)


@receiver(request_started)
def at_begining_request(sender,environ,**kwargs):
    print("-----------------")
    print("At begining Request")
    print("sender",sender)
    print("environ" ,environ)
    print("Kwargs" , kwargs)

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("-----------------")
    print("At ending Request")
    print("sender",sender)
    print("Kwargs" , kwargs)


@receiver(got_request_exception)
def at_request_exception(sender,request,**kwargs):
    print("-----------------")
    print("At Request Exception")
    print("sender",sender)
    print("environ" ,request)
    print("Kwargs" , kwargs)

