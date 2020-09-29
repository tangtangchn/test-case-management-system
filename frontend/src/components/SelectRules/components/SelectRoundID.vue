<template>
  <div class="select-round">
    <el-select
      v-model="valueRound"
      filterable
      placeholder="选择或搜索轮次编号"
      size="large"
      :change="changeSelection()">
      <el-option
        v-for="item in optionsRound"
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
      optionsRound: [{
        value: '1',
        label: '第一轮 (-1)'
      }, {
        value: '2',
        label: '第二轮 (-2)'
      }, {
        value: '3',
        label: '第三轮 (-3)'
      }],
      valueRound: ''
    }
  },
  methods: {
    changeSelection: function () {
      // 向兄弟组件【ImportTable】传值
      bus.$emit('newRound', this.valueRound)
    }
  }
}
</script>
