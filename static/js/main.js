
    let searchForm = document.getElementById('searchForm')
    let pageLinks = document.getElementsByClassName('page-link')

    //Ensure Search form exists
    if (searchForm) {
        Array.from(pageLinks).forEach(pageLink => {
            pageLink.addEventListener('click', function (e) {
                e.preventDefault();
                
                //Get the data attribute
                let page = this.dataset.page 
                console.log('PAGE:', page)

                //Add hidden search Input to Form
                searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
                
                //submit Form
                searchForm.submit()
            });
        });
        }