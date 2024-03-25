import React from 'react'
import { CircleDollarSign } from 'lucide-react'
import { PieChart, Pie, Cell } from 'recharts'

interface dataType {
  name: string
  value: number
  color: string
}

const RADIAN = Math.PI / 180
const data = [
  { name: 'A', value: 80, color: '#808080' },
  { name: 'B', value: 20, color: '#ff4500' },
  { name: 'C', value: 20, color: '#ff0000' },
]
const cx = 100
const cy = 100
const iR = 50
const oR = 100
const value = 60

const needle = (
  value: number,
  data: dataType[],
  cx: number,
  cy: number,
  iR: number,
  oR: number,
  color: string,
) => {
  let total = 0
  data.forEach((v) => {
    total += v.value
  })
  const ang = 180.0 * (1 - value / total)
  const length = (iR + 2 * oR) / 3
  const sin = Math.sin(-RADIAN * ang)
  const cos = Math.cos(-RADIAN * ang)
  const r = 5
  const x0 = cx + 5
  const y0 = cy + 5
  const xba = x0 + r * sin
  const yba = y0 - r * cos
  const xbb = x0 - r * sin
  const ybb = y0 + r * cos
  const xp = x0 + length * cos
  const yp = y0 + length * sin

  return [
    <circle cx={x0} cy={y0} r={r} fill={color} stroke="none" key={ang} />,
    <path
      d={`M${xba} ${yba}L${xbb} ${ybb} L${xp} ${yp} L${xba} ${yba}`}
      stroke="#none"
      fill={color}
      key={ang}
    />,
  ]
}

const renderLabels = (cx: number, cy: number) => {
  const total = data.reduce((acc, curr) => acc + curr.value, 0)
  return [0, 60, 80, 100, 120].map((value, index) => {
    const percentage = value / total
    const angle = 180 - percentage * 180
    const radian = (angle * Math.PI) / 180
    const labelRadius = iR + (oR - iR) * 0.5
    const x = cx + labelRadius * Math.cos(radian)
    const y = cy - labelRadius * Math.sin(radian)
    return (
      <text
        key={`label-${index}`}
        x={x}
        y={y}
        fill="white"
        textAnchor="middle"
        dominantBaseline="central"
      >
        {value}%
      </text>
    )
  })
}

const GaugeChart: React.FC = () => {
  return (
    <div className="flex flex-col items-center gap-2 pt-4">
      <div className="flex items-center justify-center gap-2">
        <CircleDollarSign className="h-4 w-4" />
        <div className="font-bold">
          <p>回収率</p>
        </div>
      </div>
      <PieChart width={200} height={120} margin={{ top: 5 }}>
        <Pie
          dataKey="value"
          startAngle={180}
          endAngle={0}
          data={data}
          cx={cx}
          cy={cy}
          innerRadius={iR}
          outerRadius={oR}
          fill="#8884d8"
          stroke="none"
        >
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={entry.color} />
          ))}
        </Pie>
        {needle(value, data, cx, cy, iR, oR, '#FFF')}
        {renderLabels(cx, cy)}
      </PieChart>
    </div>
  )
}

export default GaugeChart
