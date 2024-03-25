'use client'

import { ThumbsUp, ScanEye } from 'lucide-react'
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
} from 'recharts'
import evaluationData from './evaluationData.json'
import featureImportance from './featureImportance.json'
import GaugeChart from './GaugeChart'
import { Separator } from '@/components/ui/separator'

export const TrainingResults = () => {
  return (
    <div className="mt-8 flex flex-col justify-center gap-4 p-4 sm:mt-0 sm:flex-row">
      <Separator className="bg-gray-700 sm:hidden" />
      <p className="mb-2 text-center text-xl font-bold sm:hidden">学習結果</p>
      <div className="flex flex-col justify-center gap-2">
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
            <PolarRadiusAxis angle={18} domain={[0, 1]} />
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
        <Separator className="bg-gray-700 sm:hidden" />
        <GaugeChart />
        <Separator className="bg-gray-700 sm:hidden" />
      </div>
      <div className="flex flex-col justify-center">
        <div>
          <div className="flex items-center justify-center gap-2">
            <ThumbsUp className="h-4 w-4" />
            <p className="text-center font-bold">特徴量重要度</p>
          </div>
          <BarChart
            width={300}
            height={400}
            data={featureImportance}
            layout="vertical"
            margin={{ top: 5, right: 10, left: 50, bottom: 5 }}
          >
            <CartesianGrid />
            <XAxis type="number" />
            <YAxis dataKey="name" type="category" />
            <Tooltip />
            <Bar dataKey="value" barSize={8} fill="#82ca9d" />
          </BarChart>
        </div>
      </div>
    </div>
  )
}
