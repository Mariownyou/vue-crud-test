<template>

  <Form :method="savePost" :post="post" />

</template>

<script>

import PostDataService from "../services/PostDataService";
import Form from "./Form"

export default {
  name: "add-post",
  components: {
    Form
  },
  data() {
    return {
      post: {
        id: null,
        title: "",
        text: "",
      },
    };
  },
  methods: {
    savePost() {
      var data = {
        title: this.post.title,
        text: this.post.text
      };

      PostDataService.create(data)
        .then(response => {
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>
