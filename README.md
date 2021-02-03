# vue-crud-test
> Тестовое задание

## Как запустить?
**Устанавливаем зависимости**

     npm install      
**Запускаем frontend**

     cd vue-crud-test
     npm run serve
**Запускаем backend**

     cd backend
     npm run index.js


## Архитектура приложения
```
 ├── App.vue
    ├── assets                 
    │   └── logo.png
    ├── components               
    │   ├── AddPost.vue          // Форма создания нового поста
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
**Пример**
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

