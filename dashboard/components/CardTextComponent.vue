<template>
    <card-component>
        <div class="level">
            <div class="level-item">
                <div class="is-widget-label">
                    <h3 class="subtitle is-spaced is-size-6-touch">
                        <b>{{ label }}</b>
                    </h3>
                    <h4 class="body is-spaced is-size-5-touch text-wrap" style="word-wrap: break-word">
                        <pre>{{ information }}</pre>
                    </h4>
                </div>
            </div>
        </div>
    </card-component>
</template>

<script>
import CardComponent from '@/components/CardComponent'
export default {
    name: 'CardText',
    components: { CardComponent },
    props: {
        information: {
            type: String,
            default: null,
        },
        label: {
            type: String,
            default: null,
        }
    }
}
</script>