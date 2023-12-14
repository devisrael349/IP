import streamlit as st

st.title('SUDOKU')
      
abcd1 = [0, 3, 0, 0] #Linha a1a2a3a4
abcd2 = [0, 0, 0, 2] #Linha b1b2b3b4
abcd3 = [3, 0, 0, 0] #linha c1c2c3c4
abcd4 = [0, 0, 1, 0] #linha d1d2d3d4
                
abcdy1 = [0,0,3,0] #linha a1b1c1d1
abcdy2 = [3,0,0,0] #linha a2b2c2d2
abcdy3 = [0,0,0,1] #linha a3b3c3d3
abcdy4 = [0,0,1,0] #linha a4b4c4d4

            

        


def ganhar():
                if ((abcd1.count(1) == 1) and (abcd1.count(2) == 1) and (abcd1.count(3) == 1) and (abcd1.count(4) == 1) \
                and (abcd2.count(1) == 1) and (abcd2.count(2) == 1) and (abcd2.count(3) == 1) and (abcd2.count(4) == 1) \
                and (abcd3.count(1) == 1) and (abcd3.count(2) == 1) and (abcd3.count(3) == 1) and (abcd3.count(4) == 1) \
                and (abcd4.count(1) == 1) and (abcd4.count(2) == 1) and (abcd4.count(3) == 1) and (abcd4.count(4) == 1) \
                and ((abcdy1.count(1)) == 1) and ((abcdy1.count(2)) == 1) and ((abcdy1.count(3)) == 1) and ((abcdy1.count(4)) == 1) \
                and ((abcdy2.count(1)) == 1) and ((abcdy2.count(2)) == 1) and ((abcdy2.count(3)) == 1) and ((abcdy2.count(4)) == 1) \
                and ((abcdy3.count(1)) == 1) and ((abcdy3.count(2)) == 1) and ((abcdy3.count(3)) == 1) and ((abcdy3.count(4)) == 1) \
                and ((abcdy4.count(1)) == 1) and ((abcdy4.count(2)) == 1) and ((abcdy4.count(3)) == 1) and ((abcdy4.count(4)) == 1)) == True:
                    return True
                else:
                    return False
                
st.subheader('tabuleiro guia')
st.text(f'{abcd1[0]} {abcd1[1]} {abcd1[2]} {abcd1[3]}\n{abcd2[0]} {abcd2[1]} {abcd2[2]} {abcd2[3]}\n{abcd3[0]} {abcd3[1]} {abcd3[2]} {abcd3[3]}\n{abcd4[0]} {abcd4[1]} {abcd4[2]} {abcd4[3]}')



                
luna1 = st.selectbox('Qual valor você quer inserir em a1: ',[1,2,3,4])
abcd1[0] = luna1 #correto
abcdy1[0] = luna1

luna2 = st.selectbox('Qual valor você quer inserir em a2: ',[1,2,3,4])
abcd1[1] = luna2 #correto
abcdy2[0] = luna2

luna3 = st.selectbox('Qual valor você quer inserir em a3: ',[1,2,3,4])
abcd1[2] = luna3
abcdy3[0] = luna3

luna4 = st.selectbox('Qual valor você quer inserir em a4: ',[1,2,3,4])
abcd1[3] = luna4
abcdy4[0] = luna4

luna5 = st.selectbox('Qual valor você quer inserir em b1: ',[1,2,3,4])
abcd2[0] = luna5
abcdy1[1] = luna5

luna6= st.selectbox('Qual valor você quer inserir em b2: ',[1,2,3,4])
abcd2[1] = luna6
abcdy2[1] = luna6
        
luna7 = st.selectbox('Qual valor você quer inserir em b3: ',[1,2,3,4])
abcd2[2] = luna7
abcdy3[1] = luna7

luna8 = st.selectbox('Qual valor você quer inserir em b4: ',[1,2,3,4])
abcd2[3] = luna8
abcdy4[1] = luna8

luna9 = st.selectbox('Qual valor você quer inserir em c1: ',[1,2,3,4])
abcd3[0] = luna9
abcdy1[2] = luna9

luna10 = st.selectbox('Qual valor você quer inserir em c2: ',[1,2,3,4])
abcd3[1] = luna10
abcdy2[2] = luna10

luna11 = st.selectbox('Qual valor você quer inserir em c3: ',[1,2,3,4])
abcd3[2] = luna11
abcdy3[2] = luna11

luna12 = st.selectbox('Qual valor você quer inserir em c4: ',[1,2,3,4])
abcd3[3] = luna12
abcdy4[2] = luna12

luna13 = st.selectbox('Qual valor você quer inserir em d1: ',[1,2,3,4])
abcd4[0] = luna13
abcdy1[3] = luna13

luna14 = st.selectbox('Qual valor você quer inserir em d2: ',[1,2,3,4])
abcd4[1] = luna14
abcdy2[3] = luna14

luna15 = st.selectbox('Qual valor você quer inserir em d3: ',[1,2,3,4])
abcd4[2] = luna15
abcdy3[3] = luna15

luna16 = st.selectbox('Qual valor você quer inserir em d4: ',[1,2,3,4])
abcd4[3] = luna16
abcdy4[3] = luna16

st.text(f'{abcd1[0]} {abcd1[1]} {abcd1[2]} {abcd1[3]}\n{abcd2[0]} {abcd2[1]} {abcd2[2]} {abcd2[3]}\n{abcd3[0]} {abcd3[1]} {abcd3[2]} {abcd3[3]}\n{abcd4[0]} {abcd4[1]} {abcd4[2]} {abcd4[3]}')
if st.button('conferir'):
                ganho = ganhar()
                if ganho == True:
                    st.text('parabéns, você ganhou :) !!!!!')    
                else:
                    st.text('incorreto, tente novamente. :(')
	
