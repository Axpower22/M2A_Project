//máscara celular
var cel = document.getElementById("cel");

var imc = new Inputmask("(99) 99999-9999");
imc.mask(cel);

//máscara telefone
var tel = document.getElementById("tel");

var iml = new Inputmask("(99) 9999-9999");
iml.mask(tel);

//máscara cpf
var cpf = document.getElementById("cpf");

var imf = new Inputmask("999.999.999-99");
imf.mask(cpf);

//máscara cnpj
var cnpj = document.getElementById("cnpj");

var imj = new Inputmask("99.999.999/9999-99");
imj.mask(cnpj);

//máscara cep
var cep = document.getElementById("cep");

var ime = new Inputmask("99999-999");
imj.mask(cep);