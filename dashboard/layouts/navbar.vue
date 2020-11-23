<template>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img
                    src="https://www.nea.gov.sg/images/default-source/our-serivces/5c8e283dd07e.jpg" alt="hawker centre"
                >
            </b-navbar-item>
        </template>
        <!-- <template slot="end">
            <b-navbar-item tag="router-link" :to="{path: '/'}">
                Home
            </b-navbar-item>

            <b-navbar-dropdown :label="'Hey, user!'">
                <b-navbar-item tag="router-link" :to="{path: '/settings'}">
                    Settings
                </b-navbar-item>
                <b-navbar-item v-on:click="logout">
                    Log out
                </b-navbar-item>
            </b-navbar-dropdown>
        </template> -->
    </b-navbar>
</template>

<script>
export default {
    props: {
    },
    methods: {
    },
    data() {
        return {
        }
    },
}
</script>

<style scoped>
    @media screen and (min-width: 1024px) {
        img {
            max-height:3rem;
        }
        nav {
            padding: 0 3rem;
        }
    }


</style>
