<template>
  <div class="select-test-type">
    <el-select
      v-model="valueTestType"
      filterable
      placeholder="选择或搜索测试类型"
      size="large"
      :change="changeSelection()">
      <el-option
        v-for="item in optionsTestType"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
  </div>
</template>

<script>
import bus from '@/assets/eventBus'

export default {
  data () {
    return {
      optionsTestType: [{
        value: '1',
        label: '环境联通测试 (-1)'
      }, {
        value: '2',
        label: '稳定性测试 (-2)'
      }, {
        value: '3',
        label: '批次功能测试 (-3)'
      }, {
        value: '4',
        label: '内部测试 (-4)'
      }],
      valueTestType: ''
    }
  },
  methods: {
    changeSelection: function () {
      // 向兄弟组件【ImportTable】传值
      bus.$emit('newTestType', this.valueTestType)
    }
  }
}
</script>
