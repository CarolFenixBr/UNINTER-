let botao = document.querySelector("#botao");
botao.style.background="blue";
let estaQuebrado= false;
let contaCliques =0;
botao.addEventListener("mouseover",e =>{
    if(estaQuebrado===false){
        botao.style.background="green";
        botao.style.color="white"
    }
});
    
botao.addEventListener("mouseout",e =>{
    if(!estaQuebrado) // ! = não  //
        botao.style.background="blue";
});

/* Posso colocar também esta função --> 
function trocaVerde(){
    botao.style.background="green";
} em vez de colocar tudo em uma linha como esta descrito acima*/

botao.addEventListener("click",e =>{

    contaCliques++;  //contaCliques= contaCliques+1;

    if(contaCliques>=10){
        botao.style.background="red";
        botao.innerHTML="quebrei";
        estaQuebrado=true;
    }
});