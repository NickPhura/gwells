<template>
  <legend>Well Summary
    <div class="float-right">
        <a v-if="show.edit" :href="url" class="hide-for-print">
          <button class="btn btn-primary mb-1">Edit</button>
        </a>
        <a v-if="analytics" onclick="ga('send', 'event', 'Button', 'print', 'Wells Summary Print'); window.print();">
          <span title="Print" class="fas fa-print fa-pull-right button hide-for-print cursor-pointer print-button"></span>
        </a>
        <a v-else onclick="window.print();">
          <span title="Print" class="fas fa-print fa-pull-right button hide-for-print cursor-pointer print-button"></span>
        </a>
    </div>
  </legend>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    analytics () {
      return !!window.ga
    },
    show () {
      return {
        edit: (!!this.config && this.config.enable_data_entry === true) && this.userRoles.submissions.edit === true
      }
    },
    url () {
      return '/gwells/submissions/' + this.wellTag + '/edit'
    },
    wellTag () {
      const wellMeta = document.head.querySelector('meta[name="well.tag_number"]')
      if (wellMeta) {
        return wellMeta.content
      }
      return null
    },
    ...mapGetters(['userRoles', 'config'])
  }
}
</script>

<style>

</style>
