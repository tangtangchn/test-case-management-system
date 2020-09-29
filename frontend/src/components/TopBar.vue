<template>
  <div class="navigation">
    <div class="nav-header">
      <h2>案 例 管 理 平 台</h2>
    </div>
    <div class="nav-bar">
      <el-menu
        class="el-menu-top"
        mode="horizontal"
        @select="handleSelect"
        backgroundColor="#2c3e50"
        textColor="#fff"
        activeTextColor="#ffd04b"
        :default-active="$route.path"
        router>
        <el-menu-item index="/">
          <i class="el-icon-menu"></i>
          <span>首 页</span>
        </el-menu-item>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-document"></i>
            <span>案 例 单 管 理</span>
          </template>
          <el-menu-item index="/generate">生成案例单</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
          <el-menu-item index="2-3">选项3</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-upload"></i>
            <span>记 录 单 管 理</span>
          </template>
          <el-menu-item index="/upload">上传记录单</el-menu-item>
          <el-menu-item index="3-2">执行记录查询</el-menu-item>
        </el-submenu>
      </el-menu>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Topbar',
  data () {
    return {
      // activeIndex: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style>
.navigation {
  position: absolute;
  width: 100%;
  height: 60px;
  background-color: #2c3e50;
  color: #fff;
}
.nav-header {
  float: left;
  margin-left: 540px;
  width: 190px;
}
.nav-bar {
  float: left;
  margin-left: 300px;
  width: 465px;
}
</style>
