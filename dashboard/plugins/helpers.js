import Vue from 'vue';

Vue.mixin({
    methods:{
        snackbarAlert(message, type, duration) {
            this.$buefy.snackbar.open({
                duration: duration,
                message: message,
                type: type,
                position: 'is-bottom-left',
                actionText: 'x',
                queue: false,
            })
        },
        toastAlert(message, type, duration) {
            this.$buefy.toast.open({
                duration: duration,
                message: message,
                type: type,
                queue: false,
            })
        }
    }
});