<template>
  <div class="top">
    <h1>{{ header }}</h1>
  </div>
</template>

<script>
export default {
  name: 'Homeheader',
  data () {
    return {
      header: '案 例 管 理 平 台'
    }
  }
}
</script>

<style>
.top {
  position: absolute;
  width: 100%;
  height: 200px;
  line-height: 160px;
  color: #fff;
  background: url("../assets/screen_bg.jpg");
  background-position: center;
}
</style>
