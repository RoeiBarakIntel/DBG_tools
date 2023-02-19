import winsound
import subprocess
import datetime
import time
import os

OS_IP = '10.23.74.39'
AMT_IP = '10.23.74.6'
CONSOLE_IP = '10.23.74.1'
PING_COMMAND = 'Ping'
PING_INTERFACE = '-S'
OS_RESPONSE = "[OS]  "
AMT_RESPONSE = "[AMT]  "
file = open(r"C:\Users\Administrator\Desktop\AMT_Connection_Test.txt", "w")


def check_connectivity(ip):
    try:
        resp = subprocess.check_output(
            [PING_COMMAND, ip, PING_INTERFACE, CONSOLE_IP],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True  # return string not bytes
        )
    except subprocess.CalledProcessError:
        resp = None
        return False, resp
    if 'TTL' not in resp:
        if 'Request timed out' in resp:
            resp = f'Request timed out'
        else:
            resp = f'Unreachable'
        return False, resp
    return True, resp


response = ""
flag = True
i = 1
try:
    while flag:

        """Check connectivity with OS"""
        OS_connectivity, OS_response = check_connectivity(OS_IP)
        if not OS_connectivity:
            OS_response = OS_RESPONSE + OS_IP + OS_response
            AMT_connectivity, AMT_response = check_connectivity(AMT_IP)
            """ If OS and AMT not connected """
            if not AMT_connectivity:
                AMT_response = AMT_RESPONSE + AMT_IP + AMT_response
                response = OS_response + '\n' + AMT_response
                today = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                file.write(response + '\t' + today + f"{i} minutes past\n")
                winsound.Beep(700, 18000)
            else:
                response = OS_response
                today = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                file.write(response + '\t' + today + f"{i} minutes past\n")
                winsound.Beep(700, 18000)

        AMT_connectivity, AMT_response = check_connectivity(AMT_IP)
        if not AMT_connectivity:
            AMT_response = AMT_RESPONSE + AMT_IP + "\t" + AMT_response
            response = AMT_response
            OS_connectivity, OS_response = check_connectivity(OS_IP)
            """ If OS and AMT not connected """
            if not OS_connectivity:
                OS_response = OS_RESPONSE + OS_IP + OS_response
                response = OS_response + '\n' + AMT_response
                today = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                file.write(response + '\t' + today + f"{i} minutes past\n")

            else:
                response = AMT_response
                today = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                file.write(response + '\t' + today + f"{i} minutes past\n")
                winsound.Beep(700, 18000)
        # Clearing the Screen
        time.sleep(60)
        os.system('cls')
        if i < 60:
            print(f"{i} minutes past")
        else:
            print(f"{int(i / 60)} Hour and {i % 60} minutes past")

        i += 1

except Exception as e:
    print(e)
    today = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    file.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
    file.write(str(e) + '\t' + today + '\n' + f"{i} minutes past\n")
    file.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    file.close()

file.close()

# print(f"{today:%B %d, %Y, %H, %M, %S}")
"""  
Check connectivity with AMT
    try:
        response = subprocess.check_output(
            [PING_COMMAND, AMT_IP, PING_INTERFACE, CONSOLE_IP],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True  # return string not bytes
        )
    except subprocess.CalledProcessError:
        response = None
    if 'TTL' not in response:
        if 'Request timed out' in response:
            response = f'[AMT] {AMT_IP} Request timed out'
        else:
            response = f'[AMT] {AMT_IP} Unreachable'
        break

"""
