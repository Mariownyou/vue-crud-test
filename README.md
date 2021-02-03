# vue-crud-test
> Тестовое задание

Запустить 
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
