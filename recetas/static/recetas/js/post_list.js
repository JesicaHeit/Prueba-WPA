function on_boton_click_entradas()
{
    $.ajax({url: "/ajax/recetas_entradas/"}).done(on_traer_resultados_entradas);

}

function on_traer_resultados_entradas(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_boton_click_carnes()
{
    $.ajax({url: "/ajax/recetas_carnes/"}).done(on_traer_resultados_carnes);
}

function on_traer_resultados_carnes(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_boton_click_pastas()
{
    $.ajax({url: "/ajax/recetas_pastas/"}).done(on_traer_resultados_pastas);
}

function on_traer_resultados_pastas(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_boton_click_veggie()
{
    $.ajax({url: "/ajax/recetas_veggie/"}).done(on_traer_resultados_veggie);
}

function on_traer_resultados_veggie(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_boton_click_sandwiches()
{
    $.ajax({url: "/ajax/recetas_sandwiches"}).done(on_traer_resultados_sandwiches);
}

function on_traer_resultados_sandwiches(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_boton_click_sopas()
{
    $.ajax({url: "/ajax/recetas_sopas"}).done(on_traer_resultados_sopas);
}

function on_traer_resultados_sopas(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_boton_click_postres()
{
    $.ajax({url: "/ajax/recetas_postres"}).done(on_traer_resultados_postres);
}

function on_traer_resultados_postres(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_boton_click_todo()
{
    $.ajax({url: "/ajax/recetas_todas"}).done(on_traer_resultados_todo);
}

function on_traer_resultados_todo(html)
{
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}

function on_pagina_cargada()
{
    var boton_traer_datos_todo = $("#boton-todas");
    boton_traer_datos_todo.bind("click", on_boton_click_todo);

    var boton_traer_datos_entradas = $("#boton-entradas");
    boton_traer_datos_entradas.bind("click", on_boton_click_entradas);

    var boton_traer_datos_carnes = $("#boton-carnes");
    boton_traer_datos_carnes.bind("click", on_boton_click_carnes);

    var boton_traer_datos_pastas = $("#boton-pastas");
    boton_traer_datos_pastas.bind("click", on_boton_click_pastas);

    var boton_traer_datos_veggie = $("#boton-veggie");
    boton_traer_datos_veggie.bind("click", on_boton_click_veggie);

    var boton_traer_datos_sandwiches = $("#boton-sandwiches");
    boton_traer_datos_sandwiches.bind("click", on_boton_click_sandwiches);

    var boton_traer_datos_sopas = $("#boton-sopas");
    boton_traer_datos_sopas.bind("click", on_boton_click_sopas);

    var boton_traer_datos_postres = $("#boton-postres");
    boton_traer_datos_postres.bind("click", on_boton_click_postres);
}

$(on_pagina_cargada);
