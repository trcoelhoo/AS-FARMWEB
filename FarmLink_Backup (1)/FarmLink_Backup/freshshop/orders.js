//adicionar as encomendas, que têm os produtos adicionados no carrinho a uma variável encomendas do local Storage

const ordersEl = document.querySelector(".orders"); //select div class rounded p-2 bg-light
const prodEl = document.querySelector(".teste");

function pr(p){
    let c=[];
    for (const element of p) {
        console.log(element.name);
        console.log(prodEl);
        eval(<hvalidate class="cardvalidate_raca">${element.name
        }</hvalidate>);
    }

}
function renderorders() {
	let orders = JSON.parse(localStorage.getItem("ORDERS")) || [];
	
	//alert(cartProducts); //cartProducts tem os produtos
    

	orders.forEach((p) => {
        let i=0;
        console.log(i);
		ordersEl.innerHTML += `
        <sectionvalidate>
			<figure class="cardvalidate">
				

				
        
        <div class="cardvalidate_hero">
        <img class="cardvalidate_img" src="https://i.pinimg.com/originals/8b/6d/b2/8b6db2ff062a4f614b04d0129bf92771.png" />
    </div>
    <div class="cardvalidate_content">
        <div class="cardvalidate_info">
            <hvalidateanimal class="cardvalidate_raca"><b>Produto</b> </hvalidateanimal>
            <hvalidate class="cardvalidate_raca">${pr(p)
            }</hvalidate>
            
            <hvalidate class="cardvalidate_raca"><b>Preço final:</b>${p[i].price}</hvalidate>
        </div>
    </div>
    <div class="cardvalidate_content2">
        <div class="cardvalidate_info">
            <hvalidateperson class="cardvalidate_raca"><b>Quantidade</b> </hvalidateperson>
            <hvalidate class="cardvalidate_raca">${p[i].numberOfUnits}</hvalidate>

        </div>
    </div>
    </figure>
    </sectionvalidate>`
    i=i+1;
    
    //mostrar essas encomendas, que estão na variável do local storage, na página do hmtl      
    }); 
    
}

renderorders(); 
                
