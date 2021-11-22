cap = cv2.VideoCapture(0) #captura a camera
close = False

while(True):
    ret, captured_frame = cap.read() #pega o frame da camera
    output_frame = captured_frame.copy() #faz a copia do frame

    img_prep = prep(captured_frame) #prepara a imagem
    
    img_filter_left_click = filter_by(img_prep, [17, 63, 84], [255, 112, 255]) #objeto cor verde - filtro baseado na cor
    contours_left_click = get_contours(img_filter_left_click) # pega as bordas a partir do filtro
    
    img_filter_right_click = filter_by(img_prep, [43, 144, 90], [199, 199, 164])#objeto cor rosa - filtro baseado na cor
    contours_right_click = get_contours(img_filter_right_click) # pega as bordas a partir do filtro
    
    img_filter_close_click = filter_by(img_prep, [23, 40, 2], [179, 255, 255])#objeto cor azul - filtro baseado na cor
    contours_close_click = get_contours(img_filter_close_click) # pega as bordas a partir do filtro
    
    img_filter_move = filter_by(img_prep, [101, 69, 149], [236, 179, 190]) #objeto cor amarelo - filtro baseado na cor
    contours_move = get_contours(img_filter_move) # pega as bordas a partir do filtro
    
    for cnt in contours_left_click: #pra cada borda do filtro, executa o clique
        area = cv2.contourArea(cnt) #pega a area total da borda
        if area> 1000: #se for maior que 1000
            add_retangle(output_frame, cnt, (255, 0, 0)) #adiciona um retangulo vermelho
            autopy.mouse.click(autopy.mouse.Button.LEFT) #clica com o botao esquerdo          
        
    for cnt in contours_right_click:
        area = cv2.contourArea(cnt)
        if area> 1000:
            add_retangle(output_frame, cnt, (252, 223, 3)) #adiciona um retangulo amarelo          
            autopy.mouse.click(autopy.mouse.Button.RIGHT)              
        
    for cnt in contours_close_click:
        area = cv2.contourArea(cnt)
        if area> 1000:            
            add_retangle(output_frame, cnt, (3, 36, 252)) #adiciona um retangulo azul
            close = True
    
    for cnt in contours_move:
        area = cv2.contourArea(cnt)
        
        if area> 109:
            add_retangle(output_frame, cnt, (0,255,0)) #adiciona um retangulo verde
            
            peri = cv2.arcLength(cnt, True)  # pega o perimetro      
            approx = cv2.approxPolyDP(cnt, 0.02* peri,True) # aproximaçao - mesma regra la de cima
            
            x_,y_, w, h = cv2.boundingRect(approx)
            x1, y1 = (int(x_+w/2) , int(y_+h/2))  #pega a coordenada do centro do quadrado 
            
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr)) #pega a intersecção do eixo x baseada na largura da camera com a largura da tela
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr)) #pega a intersecção do eixo y baseada na altura da camera com a altura da tela

            # Calcula o movimento que vai fazer
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Movimento do mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(output_frame, (x1, y1), 15, (255, 0, 255), cv2.FILLED) #insere um circulo na coordenada que ta usando
            plocX, plocY = clocX, clocY # salva as infos
       

    cv2.imshow('frame', output_frame) #retorna a camera com as infos
    if cv2.waitKey(1) & 0xFF == ord('q'): #se quiser fechar com q
        break
        
cap.release() #liberar câmera
cv2.destroyAllWindows() #destroi todas as janelas que o cv2 abriu