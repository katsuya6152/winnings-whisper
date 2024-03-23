'use client'

import { CircleDollarSign, ThumbsUp, ScanEye, TrendingUp } from 'lucide-react'
import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  Legend,
  BarChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Bar,
  PieChart,
  Pie,
  Cell,
  AreaChart,
  Area,
} from 'recharts'
import evaluationData from './evaluationData.json'
import featureImportance from './featureImportance.json'

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

export const TrainingResults = () => {
  const areaChartData = [
    {
      name: 'Page A',
      uv: 4000,
      pv: 2400,
      amt: 2400,
    },
    {
      name: 'Page B',
      uv: 3000,
      pv: 1398,
      amt: 2210,
    },
    {
      name: 'Page C',
      uv: 2000,
      pv: 9800,
      amt: 2290,
    },
    {
      name: 'Page D',
      uv: 2780,
      pv: 3908,
      amt: 2000,
    },
    {
      name: 'Page E',
      uv: 1890,
      pv: 4800,
      amt: 2181,
    },
    {
      name: 'Page F',
      uv: 2390,
      pv: 3800,
      amt: 2500,
    },
    {
      name: 'Page G',
      uv: 3490,
      pv: 4300,
      amt: 2100,
    },
  ]
  return (
    <div className="flex gap-8 p-4">
      <div className="flex flex-col justify-between gap-2">
        <div>
          <div className="flex items-center justify-center gap-2">
            <ScanEye className="h-4 w-4" />
            <p className="text-center font-bold">評価指標</p>
          </div>
          <RadarChart
            outerRadius={90}
            width={350}
            height={250}
            data={evaluationData}
            margin={{ right: 20 }}
          >
            <PolarGrid />
            <PolarAngleAxis dataKey="evaluation" />
            <PolarRadiusAxis angle={30} domain={[0, 1]} />
            <Radar
              name="v0.0"
              dataKey="previous"
              stroke="#8884d8"
              fill="#8884d8"
              fillOpacity={0.6}
            />
            <Radar
              name="v0.1"
              dataKey="new"
              stroke="#82ca9d"
              fill="#82ca9d"
              fillOpacity={0.6}
            />
            <Legend />
          </RadarChart>
        </div>
        <div>
          <AreaChart
            width={300}
            height={200}
            data={areaChartData}
            margin={{
              top: 10,
              right: 10,
              left: 10,
              bottom: 10,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Area
              type="monotone"
              dataKey="uv"
              stroke="#8884d8"
              fill="#8884d8"
            />
          </AreaChart>
          <div className="flex items-center justify-center gap-2">
            <TrendingUp className="h-4 w-4" />
            <div className="font-bold">
              <p>AUC-ROC</p>
            </div>
          </div>
        </div>
      </div>
      <div className="flex flex-col justify-between">
        <div>
          <div className="flex items-center justify-center gap-2">
            <ThumbsUp className="h-4 w-4" />
            <p className="text-center font-bold">特徴量重要度</p>
          </div>
          <BarChart
            width={300}
            height={300}
            data={featureImportance}
            layout="vertical"
            margin={{ top: 5, right: 10, left: 50, bottom: 5 }}
          >
            <CartesianGrid />
            <XAxis type="number" />
            <YAxis dataKey="name" type="category" />
            <Tooltip />
            <Bar dataKey="value" barSize={8} fill="#8884d8" />
          </BarChart>
        </div>
        <div className="flex flex-col items-center gap-2">
          <PieChart width={200} height={100} margin={{ top: 20 }}>
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
          </PieChart>
          <div className="flex items-center justify-center gap-2">
            <CircleDollarSign className="h-4 w-4" />
            <div className="font-bold">
              <p>回収率</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
