const highlightedItems = document.querySelectorAll("li.added_product")
console.log(highlightedItems)
var a = document.getElementsByClassName("added_product")
var i = a.length;
for (let index = 0; index < i; index++) {
    console.log(a[index])
    a[index].addEventListener("click",function onclick() {
        const empty_context = ''
        let post_modal = document.getElementById('post-modal');
        console.log(post_modal.innerHTML)
        post_modal.replaceChildren(empty_context);
        async function postData(url) {
            // Default options are marked with *
            const response = await fetch(url, {
                method: 'GET', // *GET, POST, PUT, DELETE, etc.
                // headers: {
                //     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzQzMzc0LCJpYXQiOjE2NjUyNTQxMzcsImp0aSI6ImMxNWZiY2U0ZTI5MjQ1ZTBhMzc5MDAwYWYwNjdmOTM1IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJjYXZpZCJ9.lYcMvNptQYG3c06ppJva55MuQhHSuCt3FtmYtSbto-g'
                // }
            });
            return response.json(); // parses JSON response into native JavaScript objects
        }
        postData('http://localhost:8000/api/product/')
            .then((data) => {
                console.log(data.length); // JSON data parsed by `data.json()` call
                let post_modal = document.getElementById('post-modal');
                console.log(data);
                for (let k = 0; k < data.length;) {
                    console.log(k)
                    console.log(index)
                    if (k == index){
                        let element_id = data[k]
                        console.log(data[k])
                        post_modal.innerHTML += `
                    <div class="modal-product">
                        <!-- Start product images -->
                            <div class="product-images">
                                <div class="main-image images">
                                    <img alt="big images" src="${element_id.img}">
                                </div>
                            </div>
                            <!-- end product images -->
                            <div class="product-info">
                                <h1>${element_id.name}</h1>
                                <div class="rating__and__review">
                                    <ul class="rating">
                                        <li><span class="ti-star"></span></li>
                                        <li><span class="ti-star"></span></li>
                                        <li><span class="ti-star"></span></li>
                                        <li><span class="ti-star"></span></li>
                                        <li><span class="ti-star"></span></li>
                                    </ul>
                                    <div class="review">
                                        <a href="#">4 customer reviews</a>
                                    </div>
                                </div>
                                <div class="price-box-3">
                                    <div class="s-price-box">
                                        <span class="old-price" id="old_price" ></span>
                                        <span class="new-price">$${element_id.new_price}</span>

                                    </div>
                                </div>
                                <div class="quick-desc">
                                    ${element_id.description}
                                </div>
                                <div class="select__color">
                                    <h2>Select color</h2>
                                    <ul class="color__list">
                                        <li class="red"><a title="Red" href="#">Red</a></li>
                                        <li class="gold"><a title="Gold" href="#">Gold</a></li>
                                        <li class="orange"><a title="Orange" href="#">Orange</a></li>
                                        <li class="orange"><a title="Orange" href="#">Orange</a></li>
                                    </ul>
                                </div>
                                <div class="select__size">
                                    <h2>Select size</h2>
                                    <ul class="color__list">
                                        <li class="l__size"><a title="L" href="#">L</a></li>
                                        <li class="m__size"><a title="M" href="#">M</a></li>
                                        <li class="s__size"><a title="S" href="#">S</a></li>
                                        <li class="xl__size"><a title="XL" href="#">XL</a></li>
                                        <li class="xxl__size"><a title="XXL" href="#">XXL</a></li>
                                    </ul>
                                </div>
                                <div class="social-sharing">
                                    <div class="widget widget_socialsharing_widget">
                                        <h3 class="widget-title-modal">Share this product</h3>
                                        <ul class="social-icons">
                                            <li><a target="_blank" title="rss" href="#" class="rss social-icon"><i
                                                            class="zmdi zmdi-rss"></i></a></li>
                                            <li><a target="_blank" title="Linkedin" href="#" class="linkedin social-icon"><i
                                                            class="zmdi zmdi-linkedin"></i></a></li>
                                            <li><a target="_blank" title="Pinterest" href="#"
                                                        class="pinterest social-icon"><i class="zmdi zmdi-pinterest"></i></a>
                                            </li>
                                            <li><a target="_blank" title="Tumblr" href="#" class="tumblr social-icon"><i
                                                        class="zmdi zmdi-tumblr"></i></a></li>
                                            <li><a target="_blank" title="Pinterest" href="#"
                                                        class="pinterest social-icon"><i class="zmdi zmdi-pinterest"></i></a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                    <div class="addtocart-btn">
                                        <a href="{% url 'cart'%}"Add to cart</a>
                                    </div>
                            </div><!-- .product-info -->
                    </div><!-- .modal-product -->
                `
                k++;
                let old_price = document.getElementById('old_price');
                    if (element_id.old_price != 'null') {
                        old_price.replaceChildren(empty_context);
                        console.log(element_id.old_price)
                        old_price.innerHTML += `$ ${element_id.old_price}`
                    }
                    } else {
                        console.log('saol')
                        k++;
                    }

                };

            });

    })

}