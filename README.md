# vue-crud-test
> Тестовое задание

Я решил использовать [Bulma](https://bulma.io) вместо Bootstrap, подключил импортом в `App.vue style 28 строчка`

     @import "https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css"

## Как запустить?
**_Ссылка_** https://happy-murdock-608181.netlify.app/


**Устанавливаем зависимости**

     npm install      
**Запускаем frontend**

     cd vue-crud-test
     npm run serve
**Запускаем backend _*Если хотите проверить функционал_**

     cd api
     pip install -r requirements.txt

     python3 manage.py makemigartions
     python3 manage.py migrate
     python3 manage.py runserver


## Архитектура приложения
```
 ├── App.vue
    ├── assets                 
    │   └── logo.png
    ├── components               
    │   ├── AddPost.vue          // Страница создания нового поста
    │   ├── EditPost.vue         // Страница едактирования поста
    │   ├── Form.vue             // Форма для создания и редактирования постов
    │   ├── Navbar.vue
    │   ├── Post.vue             // Отдельный пост
    │   └── PostList.vue         // Список постов
    ├── http-common.js           // Ссылки на API
    ├── main.js
    ├── router.js                // Пути на страницы
    └── services
        └── PostDataService.js   // Сервис для общения с бд
```

## Как это работает? 

### hhtp-common.js
Тут лежит ссылка на API и импорты *axios*, по желанию можно добавить все, что угодно связанное с API

### services/PostDataService.js
Это основной сервис для общения с базой данных, все функции для работы с backend-ом должны лежать тут.
Весь функционал прописываем здесь, потом импортируем модуль и используем в компонентах, очень удобно и практично)
**Пример:**
```javascript
import http from "@/http-common";

class PostDataService {
     // забираем все посты из бд
     getAll() {
          return http.get("/posts");
     }
}
```
### router.js
Прописываем все пути к страницам и компоненты которые мы на них вызываем
**Пример:**
```javascript
import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
     {
       path: "/",
       alias: "/posts",
       name: "posts",
       component: () => import("./components/PostList")
     },
  ]
})
```

> Теперь разберем компоненты
### Navbar
Просто вынес навиграцию в отдельный компонент чтобы было удобнее

### PostList и Post
Тут все просто, в `PostList` просто используем наш сервис чтобы получить все посты и передать их
`Post`, если не получаем ошибку.
В `Post` шаблон для карточек постов и две функции: `deletePost` и `editPost` первая использует сервис чтобы удалить пост.
Вторая, используя `Router` редиректит нас на страницу изменения поста и передает в нем `id`

### Form
Очень простой компонент, берет через *props* метод, который мы будеи использовать после нажатия на кнопку (создавать пост/ обнавлять). 
Эти методы заданы в компонентах `savePost` и `editPost` соответственно. 
После создания (обновления) поста нужно перенаправить пользователя на главную, реализуем два этих действия в функции `submit` и вызывем ее в форме в самом шаблоне
```javascript
submit() {
     const router = this.$router

     // Вызываем метод который получили из компонента
     this.method()

     // Перенаправляем пользователя на главную
     router.push({
          name: 'posts'
     })
}
``` 
Дальше отслеживаем изменения переменных: `title`, `text` с помощью `v-model` и дальше функция `submit` делает с ними что нам нужно
```html
<form @submit.prevent="submit">
  <div class="field">
     <label class="label" for="title">Title</label>
     <input v-model="post.title"/> 
  </div>

  <div class="field">
     <label class="label" for="text">Text</label>
     <input v-model="post.text"/> 
     <button>Посылаем Данные</button>
  </div>
</form>
```

### AddPost и EditPost
Похожие компоненты, для начала импортируем наш сервис и форму
```javascript
import PostDataService from '../services/PostDataService'
import Form from './Form'
```
Дальше создаем каждому свои функции
*savePost, editPost*
```javascript
// AddPost.vue
savePost() {
  var data = {
  // Берем заголовок и текст из формы
  };

  // Используем наш сервис для создания поста
  PostDataService.create(data)
     .then(response => { 
       console.log(response.data); // выводим ответ от сервера если все хорошо
     })
     .catch(e => {
       console.log(e); // если нет, то выводим ошибку
     });
},
// EditPost.vue
editPost() {
  const data = {
    // Заголовок и Текст из формы
  }
  PostDataService.update(this.id, data)
     .then(response => {
       console.log(response)
     })
     .catch(e => {
       console.log(e)
     })
}
```
Но в `EditPost` нам нужно сначала получить пост по `id`, которое нам передал компонент `Post`, для этого есть функция `getPost`
```javascript
getPost() {
  PostDataService.get(this.id) // все тот же сервис
     .then(response => {
       this.post = response.data // присваиваем отвте посту
       console.log(response.data)
     })
     .catch(e => { // работает с ошибкой
       console.log(e)
     })
},
```

