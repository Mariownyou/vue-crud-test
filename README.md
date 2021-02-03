# vue-crud-test
> Тестовое задание

## Как запустить?
Устанавливаем зависимости 

     npm install      
Запускаем frontend

     npm run serve
Запускаем backend

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
Это основной сервис для общения с базой данных, все функции для работы с backendo-ом должны лежать тут.
Весь функционал прописываем здесь, потом импортируем модуль и используем в компонентах, очень удобно и практично)
Пример: 
```javascript
     // забираем все посты из бд
     getAll() {
          return http.get("/posts");
     }
````