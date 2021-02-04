<template>
  <Form :method="editPost" :post="post"/>
</template>

<script>
import PostDataService from '../services/PostDataService'
import Form from './Form'

export default {
    components: {
        Form,
    },
    data() {
        return {
            id: this.$route.params.id,
            post: {},
        }
    },
    methods: {
        getPost() {
            PostDataService.get(this.id)
                .then(response => {
                    this.post = response.data
                    console.log(response.data)
                })
                .catch(e => {
                    console.log(e)
                })
        },
        editPost() {
            const data = {
                title: this.post.title,
                text: this.post.text
            }
            PostDataService.update(this.id, data).
                then(response => {
                    console.log(response)
                })
                .catch(e => {
                    console.log(e)
                })
        }
    },
    mounted() {
        this.getPost()
    }
}
</script>

<style>

</style>