<template>
  <div class="card mt-5" v-if="post.title">
        <div class="card-content">
            <div class="media-content">
                <p class="title is-4">{{ post.title }}</p>
            </div>

            <div class="content">
                {{ post.text }}
            </div>
        </div>
            <footer class="card-footer">
            <a @click="editPost" class="card-footer-item">Edit</a>
            <a @click="deletePost" class="card-footer-item">Delete</a>
        </footer>
    </div>
</template>

<script>
import PostDataService from '../services/PostDataService'

export default {
    props: ['post'],
    data() {
        return {
            id: this.post._id ? this.post._id :  this.post.id
        }
    },
    methods: {
        deletePost() {
            PostDataService.delete(this.id)
                .then(response => {
                    console.log(response)
                })
                .catch(e => {
                    console.log(e)
                })
        },
        editPost() {
            const router = this.$router
            router.push({
                name: 'edit',
                params: {
                    id: this.id
                },
            })
        }
    },
}
</script>

<style>

</style>