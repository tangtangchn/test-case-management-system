<template>
  <div class="container">
    <div class="nav">
      <topbar></topbar>
    </div>
    <div class="main">
    </div>
    <div class="footer">
      <pagefooter></pagefooter>
    </div>
  </div>
</template>

<script>
import TopBar from '@/components/TopBar'
import PageFooter from '@/components/PageFooter'

export default {
  name: 'Generate',
  components: {
    'topbar': TopBar,
    'pagefooter': PageFooter
  },
  data () {
    return {
      // pass
    }
  }
}
</script>

<style scoped>
.container {
  position: absolute;
  width: 100%;
  min-width: 1024px;
  min-height: 100%;
  left: 0;
  right: 0;
  top: 0;
}
.main {
  padding-bottom: 50px;
}
</style>
