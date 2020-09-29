<!-- 展示模板 -->
<template>
  <div class="container">
    <div class="header">
      <homeheader></homeheader>
    </div>
    <div class="main">
    </div>
    <div class="footer">
      <pagefooter></pagefooter>
    </div>
  </div>
</template>

<script>
// 局部注册组件
import HomeHeader from '@/components/HomeHeader'
import PageFooter from '@/components/PageFooter'

export default {
  name: 'Homepage',
  components: {
    'homeheader': HomeHeader,
    'pagefooter': PageFooter
  },
  data () {
    return {
      // pass
    }
  }
}
</script>

<!-- 样式代码 -->
<!-- Add "scoped" attribute to limit CSS to this component only -->
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
