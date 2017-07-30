/**
 * Created by Francisco Passos on 04/05/2017.
 */
$(document).ready(function () {
    $(".button-collapse").sideNav();
    $("#sidenav-overlay").addClass("reset-overlay");
    $('.tap-target').tapTarget('open');
    $('.modal').modal();
});

$(".carrega").click(function () {
    $('.button-collapse').sideNav('hide');
    $(".chamados").fadeIn(300);
});

$("#vizualizar_chamado").click(function () {
    $('.button-collapse').sideNav('hide');
    $(".chamados").fadeIn(300);
    $(".chamados").load("/chamados?p=teste");
});


$("#abrigos-ver").click(function () {
    $('.button-collapse').sideNav('hide');
    $(".chamados").fadeIn(300);
    $(".chamados").load("/cad-abrigo/");
});

function fechar() {
    $('.button-collapse').sideNav('hide');
    $(".chamados").fadeOut(300);
}

//função ocultar modal com teclado
document.onkeyup = function (e) {
    if (e.which == 27) {
        $('.button-collapse').sideNav('hide');
        $(".chamados").fadeOut(300);
    } else if (e.which == 113) {
        $('.button-collapse').sideNav('hide');
        $(".chamados").fadeIn(300);
        $(".chamados").load("/chamados");
        return false;
    } else if (e.which == 9) {
        $('.button-collapse').sideNav('show');
    }
}


$(".ocorrencias-periodo").click(function () {
    $('.button-collapse').sideNav('hide');
    $('#ocorrencias-tempo').modal('open');
});


//correios
$(document).ready(function () {

    function limpa_formulário_cep() {
        // Limpa valores do formulário de cep.
        $("#rua").val("");
        $("#bairro").val("");
        $("#cidade").val("");
        $("#uf").val("");
        $("#ibge").val("");
    }

    //Quando o campo cep perde o foco.
    $("#cep").blur(function () {

        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if (validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                $("#rua").val("...");
                $("#bairro").val("...");
                $("#cidade").val("...");
                $("#uf").val("...");
                $("#ibge").val("...");

                //Consulta o webservice viacep.com.br/
                $.getJSON("//viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {

                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#rua").val(dados.logradouro);
                        $("#bairro").val(dados.bairro);
                        $("#cidade").val(dados.localidade);
                        $("#uf").val(dados.uf);
                        $("#ibge").val(dados.ibge);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    });
});

//$(document).ready(function() {
//    $.getJSON("http://iot-acre.mybluemix.net/api/acre4", function (data) {
//        $.each(data.slice(0, 1), function (key, val) {
//           alert(val.nivel);
//
//        });
//    });
//});

    $(document).ready(function () {

        $(".total").click(function () {
            alert("Alerta emitido para todos do bairro ");
        });
    });

