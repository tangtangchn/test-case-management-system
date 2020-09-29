<template>
  <div class="select-p-f">
    <el-select
      v-model="valuePF"
      filterable
      placeholder="选择执行成功或失败"
      size="large"
      :change="changeSelection()">
      <el-option
        v-for="item in optionsPF"
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
      optionsPF: [{
        value: 'P',
        label: '成功 (_P)'
      }, {
        value: 'F',
        label: '失败 (_F)'
      }],
      valuePF: ''
    }
  },
  methods: {
    changeSelection: function () {
      // 向兄弟组件【ImportTable】传值
      bus.$emit('newPF', this.valuePF)
    }
  }
}
</script>
