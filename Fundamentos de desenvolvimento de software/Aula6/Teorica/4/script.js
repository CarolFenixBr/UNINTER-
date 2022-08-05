let paragrafo = document.querySelector("#para1");

paragrafo.addEventListener("mouseover", mudaPurple);
paragrafo.addEventListener("mouseout", mudaVermelho);

function mudaPurple(){
    paragrafo.style.background="purple";
}

function mudaVermelho(){
    paragrafo.style.background="red";
}
