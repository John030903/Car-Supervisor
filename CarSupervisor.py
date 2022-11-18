import matplotlib.pyplot as plt
import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("Style.css")

def TinhPhanTram(number,sum):
    return number/sum * 100
def Dem(Positions):
    dem_MID = 0
    dem_1LEFT = 0
    dem_2LEFT = 0
    dem_3LEFT = 0
    dem_4LEFT = 0
    dem_1RIGHT = 0
    dem_2RIGHT = 0
    dem_3RIGHT = 0
    dem_4RIGHT = 0
    sum_pos = 0
    for line in Positions:
        if line == '00011000':
            dem_MID += 1
        if line == '00010000':
            dem_1LEFT += 1
        if line == '00100000' or line == '00110000':
            dem_2LEFT += 1
        if line == '01000000' or line == '01100000' or  line == '01110000':
            dem_3LEFT += 1
        if line == '10000000' or line == '11000000' or line == '11100000' or line == '11110000':
            dem_4LEFT += 1

        if line == '00001000':
            dem_1RIGHT += 1
        if line == '00000100' or line == '00001100':
            dem_2RIGHT += 1
        if line == '00000010' or line == '00000110' or  line == '00001110':
            dem_3RIGHT += 1
        if line == '00000001' or line == '00000011' or line == '00000111' or line == '00001111':
            dem_4RIGHT += 1
    percents = [dem_MID,dem_1LEFT+dem_1RIGHT,dem_2LEFT+dem_2RIGHT,dem_3LEFT+dem_3RIGHT,dem_4RIGHT+dem_4LEFT]
    sum_pos = sum(percents)
    print(sum_pos)
    percents = [TinhPhanTram(i,sum_pos) for i in percents]
    return percents



st.title('CAR SUPERVISOR')
form = st.form("my_form")
with form.container():
    Sample, Test = st.columns((1,1))
    with Sample:
        sample = st.text_input('Mẫu',placeholder='00011000 00011000')
    with Test:
        test = st.text_input('So sánh',placeholder='00011000 00010000')
    form.form_submit_button("So Sánh")
if st.session_state['FormSubmitter:my_form-So Sánh']:
    sample = sample.split()
    test = test.split()
    labels = ['MID','1','2','3','4']
    colors = ['#58e319','#58e319','#ee4c7d','#AEA2C5','#AEA2C5']
    fig, (ax1, ax2) = plt.subplots(1, 2)
    percents = Dem(sample)
    ax1.pie(percents,labels=labels,autopct='%1.1f%%',explode=[0.02,0,0,0,0],colors=colors)
    ax1.set_title( 'Mẫu:\n\nMức MID, 1: ' +str(round(percents[0]+percents[1],1)) + '\nMức 3, 4: ' +str(round(percents[3]+percents[4],1)))

    percents = Dem(test)
    ax2.pie(percents,labels=labels,autopct='%1.1f%%',explode=[0.02,0,0,0,0],colors=colors)
    ax2.set_title( 'Test:\n\nMức MID, 1: ' +str(round(percents[0]+percents[1],1)) + '\nMức 3, 4: ' +str(round(percents[3]+percents[4],1)))
    st.pyplot(fig)