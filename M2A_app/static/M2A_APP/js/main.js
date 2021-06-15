//máscara celular
var cel = document.getElementById("cel");

var imc = new Inputmask("(99) 99999-9999");
if(cel){
    imc.mask(cel);
}

//máscara telefone
var tel = document.getElementById("tel");

var iml = new Inputmask("(99) 9999-9999");
if(tel){
    iml.mask(tel);
}

//máscara fax
var fax = document.getElementById("fax");

var imx = new Inputmask("(99) 9999-9999");
if(fax){
    imx.mask(fax);
}

//máscara cpf
var cpf = document.getElementById("cpf");

var imf = new Inputmask("999.999.999-99");
if(cpf){
    imf.mask(cpf);
}

//máscara cnpj
var cnpj = document.getElementById("cnpj");

var imj = new Inputmask("99.999.999/9999-99");
if(cnpj){
    imj.mask(cnpj);
}

//máscara cep
var cep = document.getElementById("cep");

var ime = new Inputmask("99999-999");
if(cep){
    ime.mask(cep);
}