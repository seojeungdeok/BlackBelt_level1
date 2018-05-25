#!/usr/bin/python

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

sessions = Sessions_Attended["sessions"]
session_list = sessions.split(",")
session_list_len = len(session_list)
print("I have attended "+str(session_list_len)+" sessions!!")
#print(len(session_list))
#for session in session_list:
#    print(session)
#I have attended 2 sessions!!