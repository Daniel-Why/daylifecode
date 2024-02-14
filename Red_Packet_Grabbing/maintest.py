# 微信抢红包
#%%
import time
import pyautogui as pya
import do_operations as do
import keyboard
import pyautogui as pya
# %%
packet_message_pic = r".\asset\wchat\01_wc_red_packet_Grabbing\01.jpg"
packet_true_pic = r".\asset\wchat\01_wc_red_packet_Grabbing\02.jpg"
packet_message_close_pic = r".\asset\wchat\01_wc_red_packet_Grabbing\03.jpg"
go_back_pic=r".\asset\wchat\01_wc_red_packet_Grabbing\04.jpg"
already_get_pic=r".\asset\wchat\01_wc_red_packet_Grabbing\05.jpg"
already_get_pic2=r".\asset\wchat\01_wc_red_packet_Grabbing\06.jpg"
failure_get_pic=r".\asset\wchat\01_wc_red_packet_Grabbing\07.jpg"

def go_back():
    print(do.fine_click(go_back_pic))
    print("back")
#%%  

while True:
    #if keyboard.is_pressed('home'): 
    #    break
    print("监听中:",time.time())
    packet_location = do.fine_location(packet_message_pic)
    if packet_location != 0:
        do.mouse_click(packet_location)
        start_time = time.time()
        while (time.time()-start_time)<2:
            open_icon_location=do.fine_location(packet_true_pic)
            if open_icon_location != 0:
                do.mouse_click(open_icon_location)
                print('抢到红包')
                time.sleep(0.3)
                do.keyboard_press("esc")
                time.sleep(0.2)
                break
        else:
            time.sleep(0.2)
            do.keyboard_press("esc")
            time.sleep(0.2)

    else:
        if do.fine_location(already_get_pic) != 0:
            do.fine_click(already_get_pic2)
            do.keyboard_press("esc")
            print("红包已经抢过")
            time.sleep(0.2)

        elif do.fine_location(failure_get_pic) !=0:
            do.keyboard_press("esc")
            print("未抢到红包")
            time.sleep(0.2)
        else:
            pass

# %%
