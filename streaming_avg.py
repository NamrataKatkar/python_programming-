import datetime
streams = [[1000, 123, 1, datetime.datetime(2014, 4, 11, 8, 0)],
[1000, 123, 2, datetime.datetime(2014, 4, 11, 8, 10)],
[1000, 123, 3, datetime.datetime(2014, 4, 11, 8, 20)],
[1000, 123, 4, datetime.datetime(2014, 4, 11, 8, 30)],
[1000, 123, 5, datetime.datetime(2014, 4, 11, 8, 31)],
[1001, 125, 1, datetime.datetime(2014, 4, 11, 9, 10)],
[1001, 125, 2, datetime.datetime(2014, 4, 11, 9, 30)],
[1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 50)],
[1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 51)],[1001, 125, 4, datetime.datetime(2014, 4, 11, 9, 52)],
[1005, 129, 1, datetime.datetime(2014, 4, 11, 9, 8)],[1005, 129, 2, datetime.datetime(2014, 4, 11, 9, 10)],
[1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 12)],[1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 13)],
[1005, 129, 4, datetime.datetime(2014, 4, 11, 9, 14)],[1005, 129, 5, datetime.datetime(2014, 4, 11, 9, 18)]]

res={}
no_of_users={1:0,2:0,3:0,4:0}
step_avg={1:0,2:0,3:0,4:0}

for i in range(len(streams)):
    stream=streams[i]
    session_id,user_id,step_id,current_timestamp=stream
    #print(stream)
    if ((session_id,user_id,step_id) not in res.keys()):
        res[(session_id,user_id,step_id)]=current_timestamp
    if step_id>1 and (session_id,user_id,step_id-1) in res:
        prev_timestamp=res[(session_id,user_id,step_id-1)]
        total_time_spent_on_stepMinus1=(current_timestamp-prev_timestamp).total_seconds()
        step_avg[step_id-1]+=total_time_spent_on_stepMinus1
        no_of_users[step_id-1]+=1

print(step_avg)
print(no_of_users)
            
for key,val in step_avg.items():
    avg=val/(no_of_users[key])
    print("avg of step {} is {}".format(key,avg))

