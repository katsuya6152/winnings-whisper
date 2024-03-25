import { Bot } from 'lucide-react'
import raceEntries from './raceEntries.json'
import { HorseEntry } from './HorseEntry'
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'

export const Predict = () => {
  return (
    <div className="p-4">
      <div className="flex items-center justify-center gap-4">
        <div className="rounded-lg border p-2">
          <Bot className="h-4 w-4" />
        </div>
        <div className="font-bold">
          <p>予測</p>
        </div>
      </div>
      <div>
        <Accordion type="single" collapsible className="w-full">
          {raceEntries.map((entry, index) => (
            <AccordionItem key={index} value={`item-${index}`}>
              <AccordionTrigger>{entry.date}</AccordionTrigger>
              <AccordionContent className="flex flex-col gap-2">
                {entry.horses.map((horse, horseIndex) => (
                  <HorseEntry key={horseIndex} index={horseIndex} {...horse} />
                ))}
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </div>
    </div>
  )
}
