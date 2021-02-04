# vue-crud-test
> Тестовое задание

Я решил использовать [Bulma](https://bulma.io) вместо Bootstrap, подключил импортом в `App.vue style 28 строчка`

     @import "https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css"

## Как запустить?
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
Тут лежит ссылка на API и импорты axios, по желанию можно добавить все, что угодно связанное с API

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

