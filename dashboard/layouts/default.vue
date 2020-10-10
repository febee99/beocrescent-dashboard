<template>
    <div class="container-fluid" style="min-height: 100vh;">
        <navbar/>
        <nuxt/>
    </div>
</template>

<script>
import navbar from '@/layouts/navbar.vue'

export default {
    head: {
        link: [
            { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Istok+Web:wght@400;700&family=Rubik:wght@300;400;500;700&display=swap' },
            { rel: 'stylesheet', href: 'https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css' },
        ],
    },
    data () {
        return {
            mobile: false,
        }
    },
    components: {
        navbar
    },
}
</script>
