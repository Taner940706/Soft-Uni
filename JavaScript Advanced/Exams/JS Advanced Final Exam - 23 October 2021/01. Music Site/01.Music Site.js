function solve() {
    //TODO

    const allHitsField = document.querySelector('.all-hits-container');
    const likeField = document.querySelector('.likes p');
    const saveField = document.querySelector('.saved-container');

    const genreField = document.getElementById('genre');
    const nameField = document.getElementById('name');
    const authorField = document.getElementById('author');
    const dateField = document.getElementById('date');
    const addButton = document.getElementById('add-btn');

    addButton.addEventListener('click', addNewSong);

    function addNewSong(e) {
        e.preventDefault();

        const genre = genreField.value;
        const name = nameField.value;
        const author = authorField.value;
        const date = dateField.value;

        if (genre === '' || name === '' || author === '' || date === '') {
            return;
        }

        const div = document.createElement('div');
        div.className = 'hits-info';

        const img = document.createElement('img');
        img.src = './static/img/img.png';

        const h1 = document.createElement('h2');
        h1.textContent = `Genre: ${genre}`;
        const h2 = document.createElement('h2');
        h2.textContent = `Name: ${name}`;
        const h3 = document.createElement('h2');
        h3.textContent = `Author: ${author}`;
        const h4 = document.createElement('h3');
        h4.textContent = `Date: ${date}`;

        const saveBtn = document.createElement('button');
        saveBtn.className = 'save-btn';
        saveBtn.textContent = 'Save song';
        saveBtn.addEventListener('click', saveSong);

        const likeBtn = document.createElement('button');
        likeBtn.className = 'like-btn';
        likeBtn.textContent = 'Like song';
        likeBtn.addEventListener('click', likeSong);

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'Delete';
        deleteBtn.addEventListener('click', deleteSong);

        div.appendChild(img);
        div.appendChild(h1);
        div.appendChild(h2);
        div.appendChild(h3);
        div.appendChild(h4);
        div.appendChild(saveBtn);
        div.appendChild(likeBtn);
        div.appendChild(deleteBtn);

        allHitsField.appendChild(div);

        genreField.value = '';
        nameField.value = '';
        authorField.value = '';
        dateField.value = '';

        function saveSong(e) {
            e.target.parentElement.remove();

            const div = document.createElement('div');
            div.className = 'hits-info';

            const img = document.createElement('img');
            img.src = './static/img/img.png';

            const h1 = document.createElement('h2');
            h1.textContent = `Genre: ${genre}`;
            const h2 = document.createElement('h2');
            h2.textContent = `Name: ${name}`;
            const h3 = document.createElement('h2');
            h3.textContent = `Author: ${author}`;
            const h4 = document.createElement('h3');
            h4.textContent = `Date: ${date}`;

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'Delete';
            deleteBtn.addEventListener('click', deleteSong);

            div.appendChild(img);
            div.appendChild(h1);
            div.appendChild(h2);
            div.appendChild(h3);
            div.appendChild(h4);

            div.appendChild(deleteBtn);

            saveField.appendChild(div);
        }
    }

    function likeSong(e) {
        e.target.disabled = true;
        let totalLike = likeField.textContent.replace('Total Likes: ', '');
        totalLike = Number(totalLike);
        totalLike++;

        likeField.textContent = `Total Likes: ${totalLike}`;
    }

    function deleteSong(e) {
        e.target.parentElement.remove();
    }
}