import streamlit as st
from barfi import st_barfi, Block

sample01 = Block(name='Input')
sample01.add_option(name='input display',type='display',value='数値を入力せよ1')
sample01.add_option(name='Vinput',type='input')
sample01.add_output(name='Voutput',value = 'none')

def test_func(self):
    file_path = self.get_option(name='Vinput')   
    outdata = str(file_path) + str(' cal done')
    st.write(outdata)
sample01.add_compute(test_func)
st_barfi(base_blocks=[sample01])
