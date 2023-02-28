
var radios = document.getElementsByName('filtrocategoria')
for ( var i = 0; i < radios.length; i++){
  radios[i].addEventListener('click', e => {render_cat(e)})
}

function render_cat (e)
{
  fetch("/api/1/" + e.target.value)
    .then( response => response.json() )
    .then( d =>{
      h = ""
      for(var i = 0; i < d.length; i++){
        var p = `
        <div class="card">
          <img src="../staticFiles/img/appleygreen.png" alt="Product">
          <h3>`+ d[i].name +`</h3>
          <p class="precio">`+d[i].price+`</p>
        </div>
        `
        h = h + p
      }
      return h
    })
    .then( f => {
      grid = document.getElementById('product-grid').innerHTML = f
    })
}
