<template>

    <Form :method="savePost" :post="post" />

</template>

<script>

import PostDataService from "../services/PostDataService";
import Form from "./Form"

export default {
  name: "add-post",
  data() {
    return {
      post: {
        id: null,
        title: "",
        text: "",
      },
      submitted: false
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
          this.post.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
  },
  components: {
    Form
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>
