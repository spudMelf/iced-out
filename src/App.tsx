import { Button } from "./components/ui/button";
import { Separator } from "@/components/ui/separator";
import { Textarea } from "@/components/ui/textarea";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function App() {
  const [mode, setMode] = useState(1);
  const [reuslts, setResults] = useState("These are the results");

  function handleClick(
    mode: number
  ): React.MouseEventHandler<HTMLButtonElement> | undefined {
    if (mode == 1) {
      // do one
    } else if (mode == 2) {
      // do this
    } else if (mode == 3) {
      // do this
    }

    return undefined;
  }

  function handleClick2(
    num: number
  ): React.MouseEventHandler<HTMLButtonElement> | undefined {
    // setMode(num);
    return undefined;
  }

  return (
    <div className="flex h-screen bg-[#09090B]">
      <main className="m-auto border-1 w-[75%] h-[75%] border-2 border-[#27272A] rounded-lg">
        <div className="flex justify-between align-middle p-2">
          <Input
            disabled
            type="email"
            placeholder="Title"
            className="w-[200px] bg-[#09090B] border-0 text-3xl text-[#E2E2E2]"
          />
          <div className="flex gap-2">
            <Input
              placeholder="Email"
              className="bg-[#212124] border-[#27272A]"
            />
            <Button className="bg-[#212124] p-2" onClick={handleClick2(1)}>
              Button 1
            </Button>
            <Button className="bg-[#212124] p-2" onClick={handleClick2(2)}>
              Button 1
            </Button>
            <Button className="bg-[#212124] p-2" onClick={handleClick2(3)}>
              Button 1
            </Button>
          </div>
        </div>
        <Separator className="bg-[#212124]" />
        <div className="flex p-4 h-[92.5%] gap-4">
          <div className="w-[1000px] h-[800px]">
            {mode == 1 ? (
              <Textarea
                className="grow block w-[1000px] h-[650px] my-2 bg-[#09090B] border-[#27272A]"
                placeholder="'Enter your your text here'"
              />
            ) : mode == 2 ? (
              <Textarea className="grow block w-[1000px] h-[650px] my-2 bg-[#09090B] border-[#27272A]" />
            ) : (
              <div className="grow block w-[1000px] h-[650px] my-2 bg-[#09090B] border-[#27272A]">
                <Label htmlFor="picture">Picture</Label>
                <Input
                  id="picture"
                  type="file"
                  className="h-[630px] bg-[#09090B]"
                />
              </div>
            )}
            <Button
              className="bg-[#212124] w-[1000px]"
              onClick={handleClick(mode)}
            >
              Submit
            </Button>
          </div>
          <div>
            <Textarea
              className="grow block w-[390px] h-[700px] my-2 bg-[#09090B] border-[#27272A] text-[#E2E2E2] text-inherit text-3xl"
              placeholder={reuslts}
            />
          </div>
        </div>
      </main>
    </div>
  );
}
