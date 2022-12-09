// var a = document.getElementsByClassName("tag_selector")
// var i = a.length;
// for (let index = 0; index < i;index++) {
//     console.log(a[index])
//     a[index].addEventListener("click",function onclick(e) {
//         e.preventDefault();
//         var tag = a[index].innerHTML
//         console.log(tag)
//         const empty_context = ''
//         let tag_model = document.getElementById('products_with_tag');
//         tag_model.replaceChildren(empty_context);

//         console.log("hello")// Example POST method implementation:
//         async function postData(url) {
//             // Default options are marked with *
//             const response = await fetch(url, {
//                 method: 'GET', // *GET, POST, PUT, DELETE, etc.
//                 // headers: {
//                 //     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzQzMzc0LCJpYXQiOjE2NjUyNTQxMzcsImp0aSI6ImMxNWZiY2U0ZTI5MjQ1ZTBhMzc5MDAwYWYwNjdmOTM1IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJjYXZpZCJ9.lYcMvNptQYG3c06ppJva55MuQhHSuCt3FtmYtSbto-g'
//                 // }
//             });
//             return response.json(); // parses JSON response into native JavaScript objects
//         }
//         postData('http://localhost:8000/api/product/')
//             .then((data) => {
//             console.log('aye')
//                 console.log(data.length); // JSON data parsed by `data.json()` call
//                 console.log(data);
//                 let tag_model = document.getElementById('products_with_tag');
//                 for (let u = 0; u < data.length;u++) {
//                     console.log(u)
//                     console.log(index)
//                     tag_element = data[u]
//                     console.log(tag)
//                     tag_model.innerHTML += `
//                         <div class="col-md-3 single__pro col-lg-3 cat--1 col-sm-4 col-xs-12">
//                         <div class="product foo">
//                             <div class="product__inner">
//                                 <div class="pro__thumb">
//                                     <a href="{% url 'product_detail' ${tag_element.slug} %}">
//                                         <img src="${tag_element.img}" alt="product images">
//                                     </a>
//                                 </div>
//                                 <div class="product__hover__info">
//                                     <ul class="product__action">
//                                         <li class="added_product"><a data-toggle="modal" data-target="#productModal"
//                                                 title="Quick View" class="quick-view modal-view detail-link"
//                                                 href="#"><span class="ti-plus"></span></a></li>
//                                         <li><a title="Add TO Cart" href="{% url 'cart'%}"><span
//                                                     class="ti-shopping-cart"></span></a></li>
//                                         <li><a title="Wishlist" href="wishlist.html"><span class="ti-heart"></span></a>
//                                         </li>
//                                     </ul>
//                                 </div>
//                             </div>
//                             <div class="product__details">
//                                 <h2><a href="{% url 'product_detail'  ${tag_element.slug} %}" id='product-name'>${tag_element.name}</a></h2>
//                                 <ul class="product__price">
                                
                                    
//                                     <li class="old__price" id ='old_price'></li>
//                                     <li class="new__price">$  ${tag_element.new_price}</li>
//                                 </ul>
//                             </div>
//                         </div>
//                     </div>
//                         `
//                     let old_price = document.getElementById('old_price');
//                     if (tag_element.old_price != 'null') {
//                         old_price.replaceChildren(empty_context);
//                         console.log(tag_element.old_price)
//                         old_price.innerHTML += `$ ${tag_element.old_price}`
//                     }

                
//                 };
                

//             });

//     })
    
// }