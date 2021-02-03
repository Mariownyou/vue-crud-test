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
    {
      path: "/post/:id",
      name: "post-details",
      component: () => import("./components/Post")
    },
    {
      path: "/add",
      name: "add",
      component: () => import("./components/AddPost")
    }
  ]
});