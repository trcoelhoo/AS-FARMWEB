/* app.js */

//SELECT ELEMENTS
const productsEl = document.querySelector(".products"); //select div class products
let products_list = JSON.parse(localStorage.getItem("PRODUCTS")) || [];


//RENDER PRODUCTS
function renderProducts() {
	products_list.forEach((product) => {
		productsEl.innerHTML += `
			<div class="item">
					<div class="item-container">
						<div class="item-img">
							<img src="${product.imgSrc}" alt="${product.name}">
						</div>
						<div class="desc">
							<h2>${product.name}</h2>
							<h2><small>$</small>${product.price}</h2>
							<p> ${product.description} </p>
						</div>
						<div class="add-to-wishlist">
							<img src="./icons/heart.png" alt="add to wish list">
						</div>
						<div class="add-to-cart" onclick="addToCart(${product.id})">
							<img src="./icons/bag-plus.png" alt="add to cart">
						</div>
					</div>
			</div>
		`;
	});
}
renderProducts();
