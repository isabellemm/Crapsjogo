import random
import time

dinheiro = 1000
ficar = True
while ficar == True:
    ficar2 = True
    time.sleep(1)
    print("Você tem {0} dinheiros".format(dinheiro))
    time.sleep(1)
    
    #Se a pessoa gastar tudo, não deve mais jogar
    if dinheiro <= 0: 
        ficar = False
        print("Sinto muito, você está sem fichas. Seu dinheiro acabou. Até logo.")
        ficar = False

    else:
        continuar = input("Deseja apostar ou sair? ")    
        if continuar == "apostar" or continuar == "Apostar":
            print("Você está na fase 'Come Out'")
            time.sleep(1)
            tipoaposta = str(input("Qual tipo de aposta deseja fazer? (Pass Line Bet/Field/Any Craps/Twelve) "))
            
            #Código de Pass Line Bet
            if tipoaposta == "Pass Line Bet" or tipoaposta == "pass line bet":
                quantoaposta = int(input("Quanto deseja apostar? "))
                if quantoaposta <= 0 or quantoaposta > dinheiro:
                    print("Aposta inválida. Da próxima vez digite um valor maior que 0 e que você tenha dinheiro o suficiente para apostar")
                    time.sleep(3)
                    ficar == True
                else:
                    dado1 = random.randint(1,6)
                    dado2 = random.randint(1,6)
                    soma = dado1 + dado2
                    time.sleep(1)
                    print("A soma dos dados é...")
                    time.sleep(1)
                    print(soma)
                    time.sleep(1)
                    if soma == 7 or soma == 11:
                        dinheiro += quantoaposta
                        print("Parabéns! Você tirou {0} e ganhou".format(soma))
                        ficar == True
                    elif soma == 2 or soma == 3 or soma == 12:
                        dinheiro -= quantoaposta
                        print("Sinto muito, você tirou {0} e perdeu".format(soma))
                        ficar == True
                    
                    #Mudar da fase Come Out para a Point
                    elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
                        while ficar2 == True:
                            print("Você está na fase 'Point'. O valor de Point é {0}".format(soma))
                            time.sleep(2)
                            print("Você tem {0} dinheiros".format(dinheiro))
                            time.sleep(1)

                            #Permite que o jogador desista e saia
                            continuar2 = str(input("Deseja continuar ou sair? "))
                            if continuar2 == "sair":
                                print("Você perderá o dinheiro que apostou em Pass Line Bet")
                                dinheiro -= quantoaposta
                                time.sleep(2)
                                print("Obrigada por jogar. Você terminou com {0} dinheiros.".format(dinheiro))
                                ficar2 = False
                                ficar = False
                            
                            elif continuar2 == "continuar":
                                
                                #Possibilita que o jogador faça alguma outra aposta na fase Point
                                mais = str(input("Deseja fazer mais alguma aposta? (n/Any Craps/Field/Twelve) "))
                                

                                #Apenas Pass Line Bet
                                if mais == "n":
                                    print("Você está apostando {0} dinheiros em Pass Line Bet".format(quantoaposta))
                                    dado3 = random.randint(1,6)
                                    dado4 = random.randint(1,6)
                                    soma2 = dado3 + dado4
                                    time.sleep(2)
                                    print("A soma dos dados é...")
                                    time.sleep(1)
                                    print(soma2)
                                    time.sleep(1)
                                    if soma == soma2:
                                        dinheiro += quantoaposta
                                        print("Parabéns! Você tirou o valor do Point e ganhou")
                                        time.sleep(1)
                                        ficar2 = False
                                        ficar == True
                                    elif soma2 == 7:
                                        dinheiro -= quantoaposta
                                        print("Sinto muito, você tirou 7 e perdeu")
                                        ficar2 = False
                                        ficar == True
                                    else:
                                        print("Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                        time.sleep(2)
                                        ficar2 == True


                                #Any Craps e Pass Line Bet
                                elif mais == "Any Craps" or mais == "any craps":
                                    print("Você está apostando {0} dinheiros em Pass Line Bet".format(quantoaposta))
                                    time.sleep(2)
                                    apostaA = int(input("Quando deseja apostar em Any Craps? "))
                                    if apostaA <= 0 or apostaA > dinheiro:
                                        print("Aposta inválida. Da próxima vez digite um valor maior que 0 e que você tenha dinheiro o suficiente para apostar")
                                        time.sleep(3)
                                        ficar == True
                                    else:
                                        dado3 = random.randint(1,6)
                                        dado4 = random.randint(1,6)
                                        soma2 = dado3 + dado4
                                        time.sleep(2)
                                        print("A soma dos dados é...")
                                        time.sleep(1)
                                        print(soma2)
                                        time.sleep(1)
                                        if soma == soma2:
                                            dinheiro += quantoaposta - apostaA
                                            print("Pass Line Bet: Parabéns! Você tirou o valor do Point e ganhou")
                                            time.sleep(2)
                                            print("Any Craps: Sinto muito, você tirou {0} e perdeu".format(soma2))
                                            time.sleep(1)
                                            ficar2 = False
                                            ficar == True

                                        elif soma2 == 7:
                                            dinheiro += - quantoaposta - apostaA
                                            print("Pass Line Bet e Any Craps: Sinto muito, você tirou 7 e perdeu")
                                            ficar2 = False
                                            ficar == True                                                                      
                                        
                                        elif soma2 == 2 or soma2 == 12 or soma2 == 3:
                                            dinheiro += apostaA*7
                                            print("Any Craps: Parabéns! Você tirou {0} e ganhou sete vezes a sua aposta!".format(soma2))
                                            time.sleep(2)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(2)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(2)
                                            ficar2 == True

                                        else:
                                            dinheiro -= apostaA
                                            print("Any Craps: Sinto muito, você tirou {0} e perdeu".format(soma2))
                                            time.sleep(3)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(3)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(3)
                                            ficar2 == True


                                #Field e Pass Line Bet
                                elif mais == "Field" or mais == 'field':
                                    print("Você está apostando {0} dinheiros em Pass Line Bet".format(quantoaposta))
                                    time.sleep(2)
                                    apostaf = int(input("Quanto deseja apostar em Field? "))
                                    if apostaf <= 0 or apostaf > dinheiro:
                                        print("Aposta inválida. Da próxima vez digite um valor maior que 0 e que você tenha dinheiro o suficiente para apostar")
                                        time.sleep(3)
                                        ficar == True
                                    else:
                                        dado3 = random.randint(1,6)
                                        dado4 = random.randint(1,6)
                                        soma2 = dado3 + dado4
                                        time.sleep(1)
                                        print("A soma dos dados é...")
                                        time.sleep(1)
                                        print(soma2)
                                        time.sleep(1)

                                        if soma == soma2:
                                            dinheiro += quantoaposta
                                            print("Pass Line Bet: Parabéns! Você tirou o valor do Point e ganhou")
                                            time.sleep(1)
                                            if soma2 == 5 or soma2 == 6 or soma2 == 8:
                                                dinheiro -= apostaf
                                                print("Field: Sinto muito, você tirou {0} e perdeu".format(soma2))
                                                time.sleep(1)
                                                ficar2 = False
                                                ficar == True
                                            elif soma2 == 4 or soma2 == 9 or soma2 == 10:
                                                dinheiro += apostaf
                                                print("Field: Parabéns, você tirou {0} e ganhou".format(soma2))                                    
                                                time.sleep(1)
                                                ficar2 = False
                                                ficar == True

                                        elif soma2 == 7:
                                            dinheiro = dinheiro - quantoaposta - apostaf
                                            print("Field e Pass Line Bet: Sinto muito, você tirou 7 e perdeu")
                                            ficar2 = False
                                            ficar == True

                                        if soma2 == 5 or soma2 == 6 or soma2 == 8:
                                            dinheiro -= apostaf
                                            print("Field: Sinto muito, você tirou {0} e perdeu".format(soma2))
                                            time.sleep(2)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(3)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(3)
                                            ficar2 == True

                                        elif soma2 == 3 or soma2 == 4 or soma2 == 9 or soma2 == 10 or soma2 == 11:
                                            dinheiro += apostaf
                                            print("Field: Parabéns, você tirou {0} e ganhou".format(soma2))
                                            time.sleep(2)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(3)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(3)
                                            ficar2 == True

                                        elif soma2 == 2:
                                            dinheiro += apostaf*2
                                            print("Field: Parabéns, você tirou 2 e ganhou em dobro!")
                                            time.sleep(2)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(3)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(3)
                                            ficar2 == True

                                        elif soma2 == 12:
                                            dinheiro += apostaf*3
                                            print("Field: Parabéns, você tirou 12 e ganhou em triplo!")
                                            time.sleep(2)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(3)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(3)
                                            ficar2 == True


                                #Twelve e Pass Line Bet
                                elif mais == "Twelve" or mais == 'twelve':
                                    print("Você está apostando {0} dinheiros em Pass Line Bet".format(quantoaposta))
                                    time.sleep(2)
                                    apostat = int(input("Quanto deseja apostar em Twelve? "))
                                    if apostat <= 0 or apostat > dinheiro:
                                        print("Aposta inválida. Da próxima vez digite um valor maior que 0 e que você tenha dinheiro o suficiente para apostar")
                                        time.sleep(3)
                                        ficar == True
                                    else:
                                        dado3 = random.randint(1,6)
                                        dado4 = random.randint(1,6)
                                        time.sleep(1)
                                        print("A soma dos dados é...")
                                        soma2 = dado3 + dado4
                                        time.sleep(1)
                                        print(soma2)
                                        time.sleep(1)
                                        if soma == soma2:
                                            dinheiro += quantoaposta - apostat
                                            print("Pass Line Bet: Parabéns! Você tirou o valor do Point e ganhou")
                                            time.sleep(2)
                                            print("Twelve: Sinto muito, você tirou {0} e perdeu".format(soma2))
                                            time.sleep(1)
                                            ficar2 = False
                                            ficar == True
                                            
                                        elif soma2 == 7:
                                            dinheiro += - quantoaposta - apostat
                                            print("Twelve e Pass Line Bet: Sinto muito, você tirou 7 e perdeu")
                                            ficar2 = False
                                            ficar == True
                                            
                                        elif soma2 == 12:
                                            dinheiro += apostat*30
                                            print("Twelve: Parabéns!! Você tirou 12 e ganhou 30 vezes o que apostou!")
                                            time.sleep(2)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(2)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(1)
                                            ficar2 == True
                                            
                                        else:
                                            dinheiro -= apostat
                                            print("Twelve: Sinto muito, você tirou {0} e perdeu".format(soma2))
                                            time.sleep(2)
                                            print("Pass Line Bet: Não foi dessa vez. Vamos tentar de novo com a mesma aposta.")
                                            time.sleep(3)
                                            print("O jogo só voltará para a fase Come Out se você tirar 7 ou {0}".format(soma))
                                            time.sleep(3)
                                            ficar2 == True
                                                           
                                #Pessoa digitou algo diferente ao escolher tipo de aposta
                                else:
                                    print("Resposta inválida. Da próxima vez digite n ou Field ou Any Craps ou Twelve.")
                                    time.sleep(2)
                                    ficar2 == True
                            
                            #Pessoa digitou algo diferente em continuar/sair
                            else:
                                print("Resposta inválida. Da próxima vez digite 'continuar' ou 'sair'.")
                                time.sleep(2)
                                ficar2 == True


            #Código da aposta Field
            elif tipoaposta == "Field" or tipoaposta == "field":
                quantoaposta2 = int(input("Quanto deseja apostar? "))
                if quantoaposta2 <= 0 or quantoaposta2 > dinheiro:
                    print("Aposta inválida. Da próxima vez digite um valor maior que 0 e que você tenha dinheiro o suficiente para apostar")
                    time.sleep(2)
                    ficar == True
                else:
                    dado5 = random.randint(1,6)
                    dado6 = random.randint(1,6)
                    soma3 = dado5 + dado6
                    time.sleep(1)
                    print("A soma dos dados é...")
                    time.sleep(1)
                    print(soma3)
                    time.sleep(1)
                    if soma3 == 5 or soma3 == 6 or soma3 == 7 or soma3 == 8:
                        dinheiro -= quantoaposta2
                        print("Sinto muito, você tirou {0} e perdeu".format(soma3))
                        ficar == True
                    elif soma3 == 3 or soma3 == 4 or soma3 == 9 or soma3 == 10 or soma3 == 11:
                        dinheiro += quantoaposta2
                        print("Parabéns, você tirou {0} e ganhou".format(soma3))
                        ficar == True
                    elif soma3 == 2:
                        dinheiro += quantoaposta2*2
                        print("Parabéns, você tirou 2 e ganhou em dobro!")
                        ficar == True
                    elif soma3 == 12:
                        dinheiro += quantoaposta*3
                        print("Parabéns, você tirou 12 e ganhou em triplo!")
                        ficar == True
            
            #Código da aposta Any Craps
            elif tipoaposta == "Any Craps" or tipoaposta == "any craps":
                quantoaposta3 = int(input("Quanto deseja apostar? "))
                if quantoaposta3 <= 0 or quantoaposta3 > dinheiro:
                    print("Aposta inválida. Da próxima vez digite um valor maior que 0 e que você tenha dinheiro o suficiente para apostar")
                    time.sleep(2)
                    ficar == True
                else:
                    dado7 = random.randint(1,6)
                    dado8 = random.randint(1,6)
                    time.sleep(1)
                    print("A soma dos dados é...")
                    time.sleep(1)
                    soma4 = dado7 + dado8
                    print(soma4)
                    time.sleep(1)
                    if soma4 == 2 or soma4 == 12 or soma4 == 3:
                        dinheiro += quantoaposta3*7
                        print("Parabéns! Você tirou {0} e ganhou sete vezes a sua aposta!".format(soma4))
                        time.sleep(2)
                        ficar == True
                    else:
                        dinheiro -= quantoaposta3
                        print("Sinto muito, você tirou {0} e perdeu".format(soma4))
                        time.sleep(1)
                        ficar == True

            #Código da aposta Twelve
            elif tipoaposta == "Twelve" or tipoaposta == "twelve":
                quantoaposta4 = int(input("Quanto deseja apostar? "))
                if quantoaposta4 <= 0 or quantoaposta4 > dinheiro:
                    print("Aposta inválida. Da próxima vez digite um valor maior que 0 e que você tenha dinheiro o suficiente para apostar.")
                    time.sleep(3)
                    ficar == True
                else:
                    dado9 = random.randint(1,6)
                    dado10 = random.randint(1,6)
                    time.sleep(1)
                    print("A soma dos dados é...")
                    soma5 = dado9 + dado10
                    time.sleep(1)
                    print(soma5)
                    time.sleep(1)
                    if soma5 == 12:
                        dinheiro += quantoaposta4*30
                        print("Parabéns!! Você tirou 12 e ganhou 30 vezes o que apostou!")
                        ficar == True
                    else:
                        dinheiro -= quantoaposta4
                        print("Sinto muito, você tirou {0} e perdeu".format(soma5))
                        ficar == True

            #Para garantir que o jogador responda apenas o nome do tipo da aposta...
            else:
                print("Resposta inválida. Da próxima vez digite Pass Line Bet/Field/Any Craps/Twelve")
                ficar == True

        #Se o jogador quiser sair
        elif continuar == "sair" or continuar == "Sair":
            ficar = False
            print("Obrigada por jogar. Você acabou com {0} dinheiros.".format(dinheiro))

        #Para garantir que o jogador vai responder apostar ou sair
        else: 
            print("Resposta inválida. Responda 'apostar' ou 'sair'.")
            ficar == True

