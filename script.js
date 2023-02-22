const bar = document.getElementById('bar');
const nav = document.getElementById('navbar');
const close = document.getElementById('close');

if(bar){
    bar.addEventListener('click', () =>{
        nav.classList.add('active');
    })
}

if(close){
    close.addEventListener('click', () =>{
        nav.classList.remove('active');
    } )
}

const item = {
    name: "",
    quantity: "",
    cost: "",
}

const cart = {
    items: [],
    totalCost: 0
  };

  if(cart){
    function addToCart(name, quantity, cost) {
        const item = { name, quantity, cost };
        cart.items.push(item);
        cart.totalCost += cost * quantity;
      }
  }

  if(closecart){
    function removeFromCart(index) {
        const item = cart.items[index];
        cart.items.splice(index, 1);
        cart.totalCost -= item.cost * item.quantity;
      }
  }

/*shopping cart logic*/

var addToCartButton = document.getElementById('add-to-cart-button')

var itemName = addToCartButton.getAttribute('data-name');
var itemCategory = addToCartButton.getAttribute('data-category');
var itemPrice = parseFloat(addToCartButton.getAttribute('data-price')); 

